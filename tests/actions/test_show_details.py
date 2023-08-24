from pro_filer.actions.main_actions import show_details

from datetime import date

# ==============MOCK===============================
contexto_falha = {"base_path": "/src/utils/????"}
data_atual = date.today()


# ==========SUCESSO=EM=CASO=DE=ARQUIVO================
def test_show_details_file(capsys, tmp_path):
    arquivo = tmp_path / "isValidLogin.ts"
    arquivo.touch()
    mock_arquivo = {
        "base_path": str(arquivo),
    }
    show_details(mock_arquivo)
    rota = capsys.readouterr()
    assert (
        rota.out
        == """File name: isValidLogin.ts
File size in bytes: 0
File type: file
File extension: .ts
Last modified date: {}
""".format(
            data_atual
        )
    )


# ==========SUCESSO=EM=CASO=DE=DIRETORIO================
def test_show_details_directory(capsys, tmp_path):
    diretorio = tmp_path / "database"
    diretorio.touch()
    mock_dicty = {
        "base_path": str(diretorio),
    }
    show_details(mock_dicty)
    rota = capsys.readouterr()
    assert (
        rota.out
        == """File name: database
File size in bytes: 0
File type: file
File extension: [no extension]
Last modified date: {}
""".format(
            data_atual
        )
    )


# ===============FALHA===================================
def test_show_details_fail(capsys):
    show_details(contexto_falha)
    rota = capsys.readouterr()
    assert rota.out == "File '????' does not exist\n"
