import click
from evo_downloader.downloader import Downloader
from evo_downloader.gui import DownloaderGUI


@click.group()
def cli():
    """CLI for evo_downloader."""
    pass


@click.command()
@click.argument("file_urls", nargs=-1)
@click.option("--folder", default="downloads", help="Folder to save downloaded files")
@click.option("--num-threads", default=10, help="Number of threads for downloading")
def download(file_urls, folder, num_threads):
    """
    Download files from the given URLs.

    Args:
        file_urls (tuple): URLs of the files to download.
        folder (str): Folder to save the downloaded files.
        num_threads (int): Number of threads for downloading.
    """
    if not file_urls:
        click.echo("Please provide at least one file URL.")
        return

    try:
        downloader = Downloader(num_threads=num_threads)
        downloaded_files = downloader.download_files(file_urls, folder)

        for file_path in downloaded_files:
            click.echo(f"Downloaded: {file_path}")
    except Exception as e:
        click.echo(f"An error occurred during download: {e}")


@click.command()
def gui():
    """
    Launch the GUI for evo_downloader.
    """
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    gui = DownloaderGUI()
    gui.show()
    sys.exit(app.exec())


cli.add_command(download)
cli.add_command(gui)

if __name__ == "__main__":
    cli()
