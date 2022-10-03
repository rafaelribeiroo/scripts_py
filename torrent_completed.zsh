#!/usr/bin/env zsh

declare -a values=(
    'adp14m1h87utohirssr7wsz5em9msx'  # 1
    'u8d4qmpz6qyqrrw33kxr7u81833gwj'  # 2
    '0'  # 3
    'siren'  # 4
    "Torrent Complete!"  # 5
    "<b><i>${TR_TORRENT_NAME:u}</i></b> finished downloading at ${TR_TIME_LOCALTIME}. Check it in ${TR_TORRENT_DIR}"  # 6
    '1'  # 7
    'https://api.pushover.net/1/messages.json'  # 8
)

curl --silent --form-string "token=${values[1]}" \
     --form-string "user=${values[2]}"  --form-string "timestamp=$(date +%s)" \
     --form-string "priority=${values[3]}" --form-string "sound=${values[4]}" \
     --form-string "title=${values[5]}" --form-string "message=${values[6]}" \
     --form-string "html=${values[7]}" "${values[8]}"
