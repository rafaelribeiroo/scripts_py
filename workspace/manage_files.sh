#!/usr/bin/env zsh

declare -A f=(
    [user_dirs]=~/.config/user-dirs.dirs
    [null]=/dev/null
)

source "${f[user_dirs]}"

declare -a d=(
    "${XDG_DOWNLOAD_DIR}"/  # 1
    /home/"${USER}"/.local/share/Trash/files  # 2
)

has_dir=0

inotifywait --quiet --monitor "${d[1]}" --event create |
while read directory action file; do

    [[ "${file}" =~ .*torrent$ ]] \
        && transmission-gtk "${d[1]}${file}" \
        && rm --force "${d[1]}${file}"

    # [[ "${file}" =~ .*tar.gz$ ]] \
    #     && tar xvf "${d[1]}${file}" \
    #     && rm --force "${d[1]}${file}"

    # if [[ "${file}" =~ .*zip$ ]]; then

    #     unzip "${d[1]}${file}" -d "${d[1]}" &> "${f[null]}"

    #     if [[ -d "${d[1]}${file//.zip/}" ]]; then

    #         has_dir=1

    #         cd "${d[1]}${file//.zip/}" &> "${f[null]}"

    #         sub_dir=$(find "${d[1]}" -maxdepth 2 -type d | tail -1 | awk --field-separator=/ '{print $6}')

    #         [[ "${sub_dir}" ]] \
    #             && cd "${sub_dir}" &> "${f[null]}"

    #         mv ./* "${d[1]}"

    #     fi

    #     mv "${d[1]}"*720p*.srt "${d[1]}"*480p*.srt "${d[1]}"*XviD*.srt "${d[1]}"*s_tv_*.srt "${d[1]}"*[0-9].WEBRip*.srt "${d[1]}"*[0-9].REPACK*.srt "${d[1]}${file}" "${d[2]}" &> "${f[null]}"

    #     [[ "${has_dir}" -eq 1 ]] \
    #         && mv --no-clobber "${d[1]}${file//.zip/}" "${d[2]}" \
    #         && cd - &> "${f[null]}"

    # fi

done
