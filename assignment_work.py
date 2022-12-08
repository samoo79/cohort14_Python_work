import pathlib
from pathlib import Path

my_path = pathlib.Path.home()
print(my_path)
my_folder = pathlib.Path.home() / "PycharmProjects"/"cohort_fourtheen"/"super_work"
my_folder.mkdir(exist_ok=True)
work_files = [my_folder/ "file_one.txt",
              my_folder/ "file_two.img",
              my_folder/ "file_three.png"
              ]

for path in work_files:
    path.touch()
folder_work = my_path / "PycharmProjects"/"cohort_fourtheen"/"super_work"/"file_one.txt"
folder_work.mkdir(exist_ok=True)
print(folder_work.exists())
source = my_path/"PycharmProjects"/"cohort_fourtheen"/"super_work"/ "songs.img"
destination = my_path /"PycharmProjects"/"cohort_fourtheen"/"chapter_one" / "Trash" / "songs.img"
source.replace(destination)
jettison = my_folder/"file_one.txt"
jettison.unlink()