from pro_filer.actions.main_actions import show_preview

# =====================MOCK=======================
contexto_falha = {"all_files": [], "all_dirs": []}
contexto_sucesso = {
    "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
    "all_dirs": ["src", "src/utils"],
}


# ==============TESTES SUCESSO===================
def test_show_preview_sucess_case(capsys):
    show_preview(contexto_sucesso)
    rota = capsys.readouterr()
    assert (
        rota.out
        == """Found 3 files and 2 directories
First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']
First 5 directories: ['src', 'src/utils']
"""
    )


# ==============TESTES FALHA====================
def test_show_preview_fail_case(capsys):
    show_preview(contexto_falha)
    rota = capsys.readouterr()
    assert rota.out == "Found 0 files and 0 directories\n"
