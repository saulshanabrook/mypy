from typing import TypeGuard

def test_typeguard_call_on_temporary_object(capsys):
    class E:
        def __init__(self) -> None:
            pass
        def __call__(self, o: object) -> TypeGuard[int]:
            return True

    x = object()
    if E()(x):
        # This should reveal type as 'builtins.int'
        reveal_type(x)

    # Capture output
    captured = capsys.readouterr()
    assert 'Revealed type is "builtins.int"' in captured.out
