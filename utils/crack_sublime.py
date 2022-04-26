import os


sublime_binary_path = "/opt/sublime_text/sublime_text"
version_magic_string = "4126"
sz_magic_string = 4
version_magic_string_offset = 0x0002d78a # (Real offset from xxd)

is_file_read = os.access(sublime_binary_path, os.R_OK)
if not is_file_read:
    print(f"File {sublime_binary_path} is not readable. Exit!")
    exit(1)
is_file_write = os.access(sublime_binary_path, os.W_OK)
if not is_file_write:
    print(f"File {sublime_binary_path} is not writable. Only check for patch.")


f = open(sublime_binary_path, "rb")
f.seek(version_magic_string_offset)
data = f.read(sz_magic_string)
if data.decode() == version_magic_string:
    print("File matched sublime_text build 4126")
else:
    print("File doesn't have build 4126 magic string")
f.close()


offset_1 = 0x00385797 # data = 0f 84; patched = 0f 85
offset_2 = 0x0038583d # data = 74 1f; patched = 75 1f

if is_file_write:
    f = open(sublime_binary_path, "rb+")

    f.seek(offset_1)
    if f.read(2) == b"\x0f\x84":
        print("Patching first jump")
        f.seek(offset_1)
        # f.write(b"\x0f\x85")

    f.seek(offset_2)
    if f.read(2) == b"\x74\x1f":
        print("Patching second jump")
        f.seek(offset_2)
        # f.write(b"\x75")

    f.close()
else:
    f = open(sublime_binary_path, "rb")
    f.seek(offset_1)
    if f.read(2) == b"\x84\x8c":
        print("First jump is not patched")
    f.seek(offset_2)
    if f.read(2) == b"\x74\x09":
        print("Second jump is not patched")
    f.close()

print("Done")
