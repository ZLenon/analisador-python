from pro_filer.actions.main_actions import show_details

# from datetime import date
# ==============MOCK===============================
contexto_sucesso = {
    "base_path": "images/pro-filer-preview.gif",
}
contexto_falha = {"base_path": "/src/utils/????"}
# time = date.today()


# ============SUCESSO===============================
def test_show_details_file(capsys):
    show_details(contexto_sucesso)
    rota = capsys.readouterr()
    assert (
        rota.out
        == """File name: pro-filer-preview.gif
File size in bytes: 270824
File type: file
File extension: .gif
Last modified date: 2023-08-22
"""
    )


def test_show_details_directory(capsys, tmp_path):
    directory = tmp_path / "database"
    directory.mkdir()
    mock_dicty = {
        "base_path": str(directory),
    }
    show_details(mock_dicty)
    rota = capsys.readouterr()
    assert (
        rota.out
        == """File name: database
File size in bytes: 4096
File type: directory
File extension: [no extension]
Last modified date: 2023-08-24
"""
    )


# ===============FALHA===================================
def test_show_details_fail(capsys):
    show_details(contexto_falha)
    rota = capsys.readouterr()
    assert rota.out == "File '????' does not exist\n"
