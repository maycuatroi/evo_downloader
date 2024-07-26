from evo_downloader.downloader import Downloader

if __name__ == "__main__":
    downloader = Downloader(num_threads=10)

    # Example file URLs
    file_urls = [
        "http://images.cocodataset.org/annotations/image_info_test2014.zip",  # String URL
        (
            "evo_downloader.zip",
            "https://github.com/maycuatroi/evo_downloader/archive/refs/heads/main.zip",
        ),  # Tuple with file name
    ]

    downloader.download_files(file_urls, "example_folder")
