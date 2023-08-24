from pro_filer.actions.main_actions import show_details

contexto_sucesso = {
    "base_path": "images/pro-filer-preview.gif",
}
contexto_falha = {"base_path": "/src/utils/????"}


def test_show_details(capsys, tmp_path):
    show_details(contexto_sucesso)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """File name: pro-filer-preview.gif
File size in bytes: 270824
File type: file
File extension: .gif
Last modified date: 2023-08-22
"""
    )


def test_show_details_file(capsys):
    show_details(contexto_falha)
    captured = capsys.readouterr()
    assert captured.out == "File '????' does not exist\n"
