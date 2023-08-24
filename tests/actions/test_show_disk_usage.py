from pro_filer.actions.main_actions import show_disk_usage
from pro_filer.cli_helpers import _get_printable_file_path

# ==============MOCK======================================
contexto_falha = {
    "all_files": [],
}


# ==============SUCESSO======================================
def test_show_disk_sucess(capsys, tmp_path):
    # Arquivo 1 com texto
    arquivo_hello_word = tmp_path / "isValidLogin.py"
    arquivo_hello_word.touch()
    arquivo_hello_word.write_text("Hello Word!!!")
    arquivo_1 = str(arquivo_hello_word)

    # Arquivo 2 com sem nada escrito
    arquivo_vazio = tmp_path / "blank_file.py"
    arquivo_vazio.touch()
    arquivo_2 = str(arquivo_vazio)

    contexto_sucesso = {
        "all_files": [arquivo_1, arquivo_2],
    }

    show_disk_usage(contexto_sucesso)
    rota = capsys.readouterr()
    saida_1 = f"'{_get_printable_file_path(arquivo_1)}':".ljust(70)
    saida_2 = f"'{_get_printable_file_path(arquivo_2)}':".ljust(70)
    assert (
        rota.out
        == """{} 13 (100%)
{} 0 (0%)
Total size: 13
""".format(
            saida_1, saida_2
        )
    )


# ==============FAIL+=======================================
def test_show_disk_fail(capsys):
    show_disk_usage(contexto_falha)
    rota = capsys.readouterr()
    assert rota.out == "Total size: 0\n"
