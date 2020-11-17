from pydub import AudioSegment
import click


@click.command()
@click.option("-f", "--file", default=None, help="Music file you wish to restore.")
def restore(file):
    if file is not None:
        # Get the new name for the file
        tmp_string = file.split(".")
        restored_file_name = tmp_string[0] + ".wav"

        # Uncompress the old, compressed music file
        compressed_music_file = AudioSegment.from_mp3(file)
        restored_music_file = compressed_music_file.export(restored_file_name, format="wav")

    else:
        print("Please specify the music file you wish to restore.")


if __name__ == '__main__':
    restore()
