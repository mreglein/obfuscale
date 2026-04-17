from pathlib import Path
import json
import yaml
import typer

app = typer.Typer(help="ObfuScale CLI")


@app.command()
def baseline(config: str = "configs/runs/baseline.yaml"):
    """Demo baseline: creates tiny artifacts so the repo is runnable day-one."""
    cfg = {}
    p = Path(config)
    if p.exists():
        cfg = yaml.safe_load(p.read_text()) or {}
    out = Path("results/baseline")
    out.mkdir(parents=True, exist_ok=True)
    (out / "metrics.csv").write_text(
        "metric,value\nAUC,0.9990\nTPR@0.1%,0.73\nTPR@0.01%,0.40\n"
    )
    (out / "confusion_matrix.txt").write_text("[[950 50]\n [ 60 940]]\n")
    (out / "run_info.json").write_text(json.dumps({"config": cfg}, indent=2))
    print(f"Baseline demo artifacts written to {out.resolve()}")


if __name__ == "__main__":
    app()
