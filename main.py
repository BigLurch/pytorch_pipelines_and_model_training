import argparse
from pathlib import Path

from src.utils import load_yaml


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True, help="Path to config yaml")
    args = parser.parse_args()

    cfg_path = Path(args.config)
    cfg = load_yaml(str(cfg_path))

    print("Config loaded OK")
    print(cfg)


if __name__ == "__main__":
    main()
