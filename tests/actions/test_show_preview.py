from pro_filer.actions.main_actions import show_preview

# =====================MOCK=======================
contexto_falha = {"all_files": [], "all_dirs": []}
saida_falha = "Found 0 files and 0 directories\n"
contexto_sucesso = {
    "all_files": [
        "index.js",
        "index.css",
        "index.html",
        "index.ts",
        "index.js",
        "index.py",
    ],
    "all_dirs": [
        "src",
        "controller",
        "model",
        "service",
        "middleware",
        "utils",
    ],
}


# ==============TESTES SUCESSO===================
def test_show_preview_sucess_case_files(capsys):
    show_preview(contexto_sucesso)
    rota = capsys.readouterr()
    assert (
        rota.out
        == """Found 6 files and 6 directories
First 5 files: ['index.js', 'index.css', 'index.html', 'index.ts', 'index.js']
First 5 directories: ['src', 'controller', 'model', 'service', 'middleware']
"""
    )


# ==============TESTES FALHA====================
def test_show_preview_fail_case(capsys):
    show_preview(contexto_falha)
    rota = capsys.readouterr()
    assert rota.out == saida_falha
