import os, json
from flask import Flask, jsonify
import psycopg
from psycopg.rows import dict_row

DB_HOST = os.getenv("DB_HOST", "database")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASS = os.getenv("DB_PASSWORD", "supersecretpw")

app = Flask(__name__)

def get_conn():
  return psycopg.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    connect_timeout=3,
  )

@app.get("/")
def root():
  try:
    with get_conn() as conn, conn.cursor(row_factory=dict_row) as cur:
      cur.execute("SELECT now() AS db_time")
      row = cur.fetchone()
      return jsonify({
        "from": "backend",
        "db_host": DB_HOST,
        "db_time": row["db_time"].isoformat()
      })
  except Exception as e:
    return jsonify({"from": "backend", "error": str(e)}), 500

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)