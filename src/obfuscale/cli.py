import sys

import typer

app = typer.Typer(help="ObfuScale CLI")


@app.command()
def baseline(config: str = "configs/runs/baseline.yaml"):
    """Not yet implemented. There is no trained model behind this command --
    image_pipeline/byteplot.py and models/cnn_baseline.py are unimplemented
    stubs. A prior version of this command wrote fabricated metrics
    (AUC 0.9990 and a canned confusion matrix) to results/baseline/; that
    output has been removed rather than fixed. Real training work is in
    progress in the private working repo."""
    print(
        "baseline: not implemented -- no trained model exists yet. "
        "This command previously wrote fabricated demo metrics; that "
        "output has been removed rather than fixed.",
        file=sys.stderr,
    )
    raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
