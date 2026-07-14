from __future__ import annotations

import subprocess
import sys

import pytest

from hinlegacy.cli import main
from hinlegacy.decoder import encode_text, list_supported_fonts


def test_cli_help_shows_usage(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--help"])

    assert exc.value.code == 0
    captured = capsys.readouterr()
    assert "usage:" in captured.out
    assert "detect" in captured.out
    assert "decode" in captured.out
    assert "encode" in captured.out
    assert "convert" in captured.out
    assert "list-fonts" in captured.out


@pytest.mark.parametrize(
    "command",
    ["detect", "decode", "encode", "convert", "list-fonts"],
)
def test_cli_subcommand_help(command, capsys):
    with pytest.raises(SystemExit) as exc:
        main([command, "--help"])

    assert exc.value.code == 0
    captured = capsys.readouterr()
    assert "usage:" in captured.out


def test_cli_no_args_shows_top_level_help(capsys):
    exit_code = main([])

    assert exit_code == 1
    captured = capsys.readouterr()
    assert "usage:" in captured.out


def test_cli_list_fonts(capsys):
    exit_code = main(["list-fonts"])

    assert exit_code == 0
    captured = capsys.readouterr()
    output_lines = [line.strip() for line in captured.out.splitlines() if line.strip()]

    supported = list_supported_fonts()
    assert output_lines == supported
    assert "krutidev_010" in output_lines
    assert "devlys_010" in output_lines
    assert "walkman_chanakya_905" in output_lines


def test_cli_decode_known_font(capsys):
    unicode_text = "भारत एक सुंदर देश है"
    encoded = encode_text(unicode_text, "krutidev_010")

    exit_code = main(["decode", encoded, "--font", "krutidev_010"])

    assert exit_code == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == unicode_text


def test_cli_encode_known_font(capsys):
    unicode_text = "भारत"
    expected = encode_text(unicode_text, "devlys_010")

    exit_code = main(["encode", unicode_text, "--font", "devlys_010"])

    assert exit_code == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


def test_cli_detect_returns_expected_font(capsys):
    unicode_text = "कृपया यहाँ अपना नाम लिखिए"
    encoded = encode_text(unicode_text, "walkman_chanakya_905")

    exit_code = main(["detect", encoded])

    assert exit_code == 0
    captured = capsys.readouterr()
    lines = [line.strip() for line in captured.out.splitlines() if line.strip()]

    assert lines[0] == "walkman_chanakya_905"
    assert any(line.startswith("confidence:") for line in lines)
    assert any(line.startswith("method:") for line in lines)


def test_cli_convert_auto_detect(capsys):
    unicode_text = "विद्यालय में हिंदी पढ़ाई जाती है"
    encoded = encode_text(unicode_text, "krutidev_010")

    exit_code = main(["convert", encoded])

    assert exit_code == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == unicode_text


def test_cli_convert_with_explicit_font(capsys):
    unicode_text = "संविधान सभी नागरिकों को अधिकार देता है"
    encoded = encode_text(unicode_text, "devlys_010")

    exit_code = main(["convert", encoded, "--font", "devlys"])

    assert exit_code == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == unicode_text


def test_cli_decode_unknown_font_returns_error_code(capsys):
    exit_code = main(["decode", "abc", "--font", "unknown_font"])

    assert exit_code == 2
    captured = capsys.readouterr()
    assert "Error:" in captured.out
    assert "Unknown font" in captured.out


def test_cli_convert_empty_text_detection_failure(capsys):
    exit_code = main(["convert", ""])

    assert exit_code == 3
    captured = capsys.readouterr()
    assert "Detection failed:" in captured.out


def test_cli_detect_empty_text_detection_failure(capsys):
    exit_code = main(["detect", ""])

    assert exit_code == 3
    captured = capsys.readouterr()
    assert "Detection failed:" in captured.out


def test_cli_decode_requires_font_argument(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["decode", "some text"])

    assert exc.value.code == 2
    captured = capsys.readouterr()
    assert "the following arguments are required: --font" in captured.err


def test_cli_encode_requires_font_argument(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["encode", "भारत"])

    assert exc.value.code == 2
    captured = capsys.readouterr()
    assert "the following arguments are required: --font" in captured.err


def test_python_module_invocation_help():
    result = subprocess.run(
        [sys.executable, "-m", "hinlegacy", "--help"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "usage:" in result.stdout
    assert "detect" in result.stdout


def test_python_module_invocation_list_fonts():
    result = subprocess.run(
        [sys.executable, "-m", "hinlegacy", "list-fonts"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    output_lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    assert "krutidev_010" in output_lines
    assert "devlys_010" in output_lines
    assert "walkman_chanakya_905" in output_lines