from pathlib import Path
from flask import Flask, render_template, request
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data_alert_deforestasi.csv"

app = Flask(__name__)


def load_data():
    """Membaca dataset contoh dan menyiapkan kolom tanggal."""
    df = pd.read_csv(DATA_PATH)
    df["tanggal"] = pd.to_datetime(df["tanggal"], errors="coerce")
    return df.dropna(subset=["tanggal"])


def summarize(df):
    total = int(len(df))
    area = round(float(df["luas_ha"].sum()), 1) if total else 0
    avg_conf = round(float(df["keyakinan_model"].mean()), 1) if total else 0
    categories = (
        df.groupby("penyebab", as_index=False)["jumlah_alert"]
        .sum()
        .sort_values("jumlah_alert", ascending=False)
    )
    monthly = (
        df.assign(bulan=df["tanggal"].dt.strftime("%b %Y"))
        .groupby("bulan", as_index=False)["jumlah_alert"]
        .sum()
    )
    regions = (
        df.groupby("wilayah", as_index=False)
        .agg(alert=("jumlah_alert", "sum"), luas=("luas_ha", "sum"))
        .sort_values("alert", ascending=False)
    )
    return {
        "total": total,
        "area": area,
        "avg_conf": avg_conf,
        "category_labels": categories["penyebab"].tolist(),
        "category_values": categories["jumlah_alert"].astype(int).tolist(),
        "month_labels": monthly["bulan"].tolist(),
        "month_values": monthly["jumlah_alert"].astype(int).tolist(),
        "region_labels": regions["wilayah"].tolist(),
        "region_values": regions["alert"].astype(int).tolist(),
    }


@app.route("/")
def index():
    df = load_data()
    region_options = ["Semua wilayah"] + sorted(df["wilayah"].unique().tolist())
    cause_options = ["Semua penyebab"] + sorted(df["penyebab"].unique().tolist())

    selected_region = request.args.get("wilayah", "Semua wilayah")
    selected_cause = request.args.get("penyebab", "Semua penyebab")

    filtered = df.copy()
    if selected_region in df["wilayah"].unique():
        filtered = filtered[filtered["wilayah"] == selected_region]
    if selected_cause in df["penyebab"].unique():
        filtered = filtered[filtered["penyebab"] == selected_cause]

    summary = summarize(filtered)
    table = filtered.sort_values("tanggal", ascending=False).copy()
    table["tanggal_tampil"] = table["tanggal"].dt.strftime("%d %b %Y")
    records = table[[
        "tanggal_tampil", "wilayah", "penyebab", "jumlah_alert",
        "luas_ha", "keyakinan_model", "catatan"
    ]].to_dict(orient="records")

    return render_template(
        "index.html",
        summary=summary,
        records=records,
        region_options=region_options,
        cause_options=cause_options,
        selected_region=selected_region,
        selected_cause=selected_cause,
    )


if __name__ == "__main__":
    app.run(debug=True)
