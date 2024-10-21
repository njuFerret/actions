import pathlib

root = pathlib.Path(__file__).parent
version_file = root / "libraries_version.txt"
version_folder = root.joinpath("versions")
version_folder.mkdir(exist_ok=True, parents=True)

for l in version_file.open("r", encoding='utf-8').readlines():
    lib, version = l.strip().split("=")
    lib = lib.strip()
    version = version.strip()
    with version_folder.joinpath(f"{lib}").open("w", encoding='utf-8') as f:
        f.write(f'{version}')
