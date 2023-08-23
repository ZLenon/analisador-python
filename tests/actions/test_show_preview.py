from pro_filer.actions.main_actions import show_preview

# =====================MOCK=======================
contexto_falha = {"all_files": [], "all_dirs": []}
saida_falha = "Found 0 files and 0 directories\n"
contexto_sucesso_arquivos = {
    "all_files": [
        "index.js",
        "index.css",
        "index.html",
        "index.ts",
        "index.js",
    ],
    "all_dirs": ["src"],
}
contexto_sucesso_diretorios = {
    "all_files": ["controller.ts"],
    "all_dirs": ["controller", "model", "service", "middleware", "utils"],
}


# ==============TESTES SUCESSO===================
def test_show_preview_sucess_case_files(capsys):
    show_preview(contexto_sucesso_arquivos)
    rota = capsys.readouterr()
    assert (
        rota.out
        == """Found 5 files and 1 directories
First 5 files: ['index.js', 'index.css', 'index.html', 'index.ts', 'index.js']
First 5 directories: ['src']
"""
    )


def test_show_preview_sucess_case_directories(capsys):
    show_preview(contexto_sucesso_diretorios)
    rota = capsys.readouterr()
    assert (
        rota.out
        == """Found 1 files and 5 directories
First 5 files: ['controller.ts']
First 5 directories: ['controller', 'model', 'service', 'middleware', 'utils']
"""
    )


# ==============TESTES FALHA====================
def test_show_preview_fail_case(capsys):
    show_preview(contexto_falha)
    rota = capsys.readouterr()
    assert rota.out == saida_falha
