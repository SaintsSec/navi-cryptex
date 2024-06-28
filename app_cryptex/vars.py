localVersion = (1, 0, 0)


def banner():
    version = localVersion[0]
    spacing = 3
    spacing = ' ' * spacing if spacing > 0 else ''

    tag = f"  {localVersion[1]}"
    tag += f" - {localVersion[2]}" if len(localVersion) > 2 else ""

    logo = [
        f'{spacing}  _____              __         ',
        f'{spacing} / ___/_____ _____  / /______ __',
        f'{spacing}/ /__/ __/ // / _ \\/ __/ -_) \\ /',
        f'{spacing}\\___/_/  \\_, / .__/\\__/\\__/_\\_\\ ',
        f'        V:{version}/___/_/',
        ' Locks only exist to keep honest',
        '          people honest         ',
    ]
    logo_len = max([len(item) for item in logo])

    offset = ' ' * int((logo_len / 2))

    for item in logo:
        print(f'{offset}{item}')
