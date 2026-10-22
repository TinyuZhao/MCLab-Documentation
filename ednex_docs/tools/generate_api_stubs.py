#!/usr/bin/env python3
"""Generate public, implementation-free Python modules for Sphinx autodoc.

The generator runs in the firmware repository. Its output is committed with
the documentation so the public documentation tree never imports firmware
implementation files.
"""

from __future__ import annotations

import argparse
import ast
import difflib
import sys
from pathlib import Path

from blockly_services_manifest import BLOCKLY_SERVICES
from driver_api_manifest import DRIVER_API, HARDWARE_API


PUBLIC_MODULES = {
    "MCLab.ai_camera": "ports/esp32/m5stack-libs/MCLab/ai_camera.py",
    "MCLab.ai_tools": "ports/esp32/m5stack-libs/MCLab/ai_tools.py",
    "MCLab.gyro_imu": "ports/esp32/m5stack-libs/MCLab/gyro_imu.py",
    "MCLab.line_rgb": "ports/esp32/m5stack-libs/MCLab/line_rgb.py",
    "MCLab.robocar": "ports/esp32/m5stack-libs/MCLab/robocar.py",
    "modules._encoder_motor": "ports/esp32/m5stack-libs/modules/_encoder_motor.py",
    "ubt_controller": "ports/esp32/m5stack-libs/ubt_controller.py",
}


_BMI270_SOURCE = "ports/esp32/m5stack-libs/libs/bmi270.py"
_GYRO_PUBLIC_CONSTANTS = (
    "LOW_POWER_MODE",
    "NORMAL_MODE",
    "PERFORMANCE_MODE",
    "ACC_RANGE_2G",
    "ACC_RANGE_4G",
    "ACC_RANGE_8G",
    "ACC_RANGE_16G",
    "GYR_RANGE_2000",
    "GYR_RANGE_1000",
    "GYR_RANGE_500",
    "GYR_RANGE_250",
    "GYR_RANGE_125",
    "ACC_ODR_1600",
    "ACC_ODR_800",
    "ACC_ODR_400",
    "ACC_ODR_200",
    "ACC_ODR_100",
    "ACC_ODR_50",
    "ACC_ODR_25",
    "GYR_ODR_3200",
    "GYR_ODR_1600",
    "GYR_ODR_800",
    "GYR_ODR_400",
    "GYR_ODR_200",
    "GYR_ODR_100",
    "GYR_ODR_50",
    "GYR_ODR_25",
)
PUBLIC_CONSTANTS = {
    "MCLab.gyro_imu": {
        name: _BMI270_SOURCE for name in _GYRO_PUBLIC_CONSTANTS
    },
}


# These modules contain inherited APIs, transport helpers, or public-looking
# implementation methods.  The descriptor intentionally publishes a flat,
# reviewed surface instead of inferring one from every non-private name.
PUBLIC_MEMBERS = {
    "MCLab.ai_camera": {
        "classes": {
            "AiCamera": (
                "__init__",
                "init",
                "set_work_mode",
                "get_current_mode",
                "get_color_rgb",
                "set_tracking_color_id",
                "get_tracked_color_block",
                "get_tag_count",
                "get_tag",
                "get_lines",
                "get_object20_count",
                "get_object20",
                "get_qrcode",
                "get_face_count",
                "get_face",
                "get_face_attributes",
                "get_recognized_face_count",
                "get_recognized_face",
                "start_face_learning",
                "start_deep_learning",
                "get_deep_learning_result",
                "get_traffic_sign_num",
                "get_traffic_sign",
                "set_light_brightness",
                "set_light_enabled",
            ),
        },
        "constants": (),
        "functions": (),
    },
    "MCLab.ai_tools": {
        "classes": {
            "VoiceRecognize": (
                "__init__",
                "init",
                "set_voice_recognize_wakeup_timeout",
                "set_voice_recognize_loop",
                "set_voice_recognize_cb",
                "get_voice_recognize_command",
                "get_voice_recognize_wakeup_status",
                "clean_voice_recognize_wakeup_status",
                "deinit",
            ),
            "FaceDetect": (
                "__init__",
                "init",
                "get_face_number",
                "get_face_detials",
            ),
            "ColorDetect": ("__init__", "init", "get_discover_color"),
            "ColorTrack": (
                "__init__",
                "init",
                "set_track_color",
                "get_color_box_number",
                "get_color_box_detials",
            ),
            "QRCode": (
                "__init__",
                "init",
                "get_qrcode_version",
                "get_qrcode_context",
            ),
            "BarCode": (
                "__init__",
                "init",
                "get_barcode_type",
                "get_barcode_context",
            ),
            "MotionDetect": ("__init__", "init", "set_roi", "get_rate"),
            "TrafficSignal": ("__init__", "init", "get_signal"),
        },
        "constants": (),
        "functions": (),
    },
    "MCLab.gyro_imu": {
        "classes": {
            "Gyro": (
                "__init__",
                "init",
                "get_accel",
                "get_gyro",
                "get_roll_pitch_yaw",
            ),
        },
        "constants": _GYRO_PUBLIC_CONSTANTS,
        "functions": (),
    },
    "ubt_controller": {
        "classes": {
            "UBTBLECentral": (
                "__init__",
                "set_event",
                "is_connected",
                "scan",
                "connect",
                "disconnect",
                "get_button_state",
                "get_joystick_pos",
            ),
        },
        "constants": (),
        "functions": (),
    },
    "MCLab.robocar": {
        "classes": {
            "Robocar": (
                "__init__",
                "init_motor_module",
                "move_forward",
                "move_backward",
                "move_right",
                "move_left",
                "rotate_right",
                "rotate_left",
                "set_motor_angle",
                "set_motor_speed",
                "motor_stop",
                "get_encoder_count",
                "get_encoder_vin_voltage",
                "clear_encoder_count",
                "angle_task",
                "ow_line_port_init",
                "reset_line_sensor",
                "set_line_sensor_mode",
                "get_line_sensor_mode",
                "get_line_sensor_values",
                "ow_two_line_get_sensor_values",
                "ow_two_line_get_sensor_value",
                "ow_multi_line_get_sensor_values",
                "ow_multi_line_get_sensor_value",
                "ow_multi_line_led",
                "ultrasonic_port_init",
                "ultrasonic_rgb_sensor",
                "ultrasonic_rgb_color",
                "ultrasonic_rgb_color_from",
                "ultrasonic_rgb_color_all",
            ),
        },
        "constants": (),
        "functions": (),
    },
}


PUBLIC_MODULES.update(
    {module_name: entry["source"] for module_name, entry in DRIVER_API.items()}
)
PUBLIC_MEMBERS.update(
    {
        module_name: {
            "classes": entry["classes"],
            "constants": entry.get("constants", ()),
            "functions": entry.get("functions", ()),
        }
        for module_name, entry in DRIVER_API.items()
    }
)
PUBLIC_INHERITED = {
    module_name: entry.get("inherited", {})
    for module_name, entry in DRIVER_API.items()
}
PUBLIC_ALIASES = {
    module_name: entry.get("aliases", {})
    for module_name, entry in DRIVER_API.items()
}

# Board-level hardware pages publish their own reviewed surface.
PUBLIC_MODULES.update(
    {module_name: entry["source"] for module_name, entry in HARDWARE_API.items()}
)
PUBLIC_MEMBERS.update(
    {
        module_name: {
            "classes": entry["classes"],
            "constants": entry.get("constants", ()),
            "functions": entry.get("functions", ()),
        }
        for module_name, entry in HARDWARE_API.items()
    }
)
PUBLIC_INHERITED.update(
    {
        module_name: entry.get("inherited", {})
        for module_name, entry in HARDWARE_API.items()
    }
)
PUBLIC_ALIASES.update(
    {
        module_name: entry.get("aliases", {})
        for module_name, entry in HARDWARE_API.items()
    }
)

# MCLab Blockly pages publish a separately reviewed set of service APIs.
# Keep this descriptor explicit so the snapshot never scans every helper in
# the legacy service directories.
PUBLIC_MODULES.update(
    {module_name: entry["source"] for module_name, entry in BLOCKLY_SERVICES.items()}
)
PUBLIC_MEMBERS.update(
    {
        module_name: {
            "classes": entry.get("classes", {}),
            "constants": entry.get("constants", ()),
            "functions": entry.get("functions", ()),
        }
        for module_name, entry in BLOCKLY_SERVICES.items()
    }
)
PUBLIC_INHERITED.update(
    {
        module_name: entry.get("inherited", {})
        for module_name, entry in BLOCKLY_SERVICES.items()
    }
)


def docstring(node: ast.AST) -> str | None:
    value = ast.get_docstring(node, clean=False)
    return value.strip() if value else None


def safe_literal(node: ast.AST) -> str | None:
    """Return source for values that can be evaluated without imports."""

    if isinstance(node, ast.Constant):
        if node.value is Ellipsis:
            return "..."
        return repr(node.value)
    if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
        values = [safe_literal(item) for item in node.elts]
        if any(value is None for value in values):
            return None
        opening, closing = {
            ast.Tuple: ("(", ")"),
            ast.List: ("[", "]"),
            ast.Set: ("{", "}"),
        }[type(node)]
        body = ", ".join(values)
        if isinstance(node, ast.Tuple) and len(values) == 1:
            body += ","
        return opening + body + closing
    if isinstance(node, ast.Dict):
        pairs = []
        for key, value in zip(node.keys, node.values):
            key_text = safe_literal(key)
            value_text = safe_literal(value)
            if key_text is None or value_text is None:
                return None
            pairs.append(f"{key_text}: {value_text}")
        return "{" + ", ".join(pairs) + "}"
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = safe_literal(node.operand)
        return ("+" if isinstance(node.op, ast.UAdd) else "-") + value if value else None
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        if node.func.id == "const" and len(node.args) == 1 and not node.keywords:
            return safe_literal(node.args[0])
        if node.func.id in {"bytes", "bytearray"} and not node.keywords:
            args = [safe_literal(arg) for arg in node.args]
            if all(arg is not None for arg in args):
                return ast.unparse(node)
    return None


def expression(node: ast.AST) -> str:
    if node is None:
        return "..."
    literal = safe_literal(node)
    if literal is not None:
        return literal
    return f"_Default({ast.unparse(node)!r})"


def annotation(node: ast.AST | None) -> str | None:
    if node is None:
        return None
    text = ast.unparse(node)
    if isinstance(node, ast.Name) and node.id in {"bool", "bytes", "dict", "float", "int", "list", "str", "tuple"}:
        return text
    if isinstance(node, ast.Constant) and node.value is None:
        return "None"
    return repr(text)


def render_arguments(args: ast.arguments) -> str:
    positional = [*args.posonlyargs, *args.args]
    defaults = [None] * (len(positional) - len(args.defaults)) + list(args.defaults)
    rendered = []
    for item, default in zip(positional, defaults):
        value = item.arg
        if item.annotation is not None:
            value += ": " + annotation(item.annotation)
        if default is not None:
            value += "=" + expression(default)
        rendered.append(value)
    if args.posonlyargs:
        rendered.insert(len(args.posonlyargs), "/")
    if args.vararg is not None:
        value = "*" + args.vararg.arg
        if args.vararg.annotation is not None:
            value += ": " + annotation(args.vararg.annotation)
        rendered.append(value)
    elif args.kwonlyargs:
        rendered.append("*")
    for item, default in zip(args.kwonlyargs, args.kw_defaults):
        value = item.arg
        if item.annotation is not None:
            value += ": " + annotation(item.annotation)
        if default is not None:
            value += "=" + expression(default)
        rendered.append(value)
    if args.kwarg is not None:
        value = "**" + args.kwarg.arg
        if args.kwarg.annotation is not None:
            value += ": " + annotation(args.kwarg.annotation)
        rendered.append(value)
    return ", ".join(rendered)


def render_function(
    module_name: str,
    node: ast.FunctionDef | ast.AsyncFunctionDef,
    indent: str,
) -> list[str]:
    prefix = "async def" if isinstance(node, ast.AsyncFunctionDef) else "def"
    result = []
    for decorator in node.decorator_list:
        if isinstance(decorator, ast.Name) and decorator.id in {"classmethod", "staticmethod", "property"}:
            result.append(indent + "@" + decorator.id)
    signature = f"{prefix} {node.name}({render_arguments(node.args)})"
    if node.returns is not None:
        signature += " -> " + annotation(node.returns)
    result.append(indent + signature + ":")
    text = docstring(node)
    if text:
        result.append(indent + "    " + repr(text))
    result.append(indent + "    ...")
    return result


def assignment_name(node: ast.Assign | ast.AnnAssign) -> str | None:
    target = node.target if isinstance(node, ast.AnnAssign) else node.targets[0]
    return target.id if isinstance(target, ast.Name) else None


def render_class(
    module_name: str,
    node: ast.ClassDef,
    public_methods: tuple[str, ...] | None = None,
    inherited_methods: tuple[ast.FunctionDef | ast.AsyncFunctionDef, ...] = (),
    public_name: str | None = None,
) -> list[str]:
    result = [f"class {public_name or node.name}:"]
    text = docstring(node)
    body = []
    if text:
        body.append("    " + repr(text))
    methods = {
        item.name: item
        for item in node.body
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    if public_methods is not None:
        missing = set(public_methods) - methods.keys()
        if missing:
            names = ", ".join(sorted(missing))
            raise SystemExit(f"public methods not found: {node.name}: {names}")
    for item in node.body:
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if public_methods is not None:
                include = item.name in public_methods
            else:
                include = item.name == "__init__" or not item.name.startswith("_")
            if include:
                body.extend(render_function(module_name, item, "    "))
    for item in inherited_methods:
        body.extend(render_function(module_name, item, "    "))
    result.extend(body or ["    ..."])
    return result


def assignment_values(source: Path) -> dict[str, ast.AST]:
    tree = ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
    values = {}
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            name = assignment_name(node)
            if name:
                values[name] = node.value
    return values


def render_module(module_name: str, source: Path, repo_root: Path) -> str:
    tree = ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
    lines = ["# Generated by tools/generate_api_stubs.py; do not edit.", "", "class _Default:", "    def __init__(self, text):", "        self.text = text", "", "    def __repr__(self):", "        return self.text", ""]
    public_members = PUBLIC_MEMBERS.get(module_name)
    if public_members is None:
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if not node.name.startswith("_"):
                    lines.extend(render_function(module_name, node, ""))
                    lines.append("")
            elif isinstance(node, ast.ClassDef):
                if not node.name.startswith("_"):
                    lines.extend(render_class(module_name, node))
                    lines.append("")
            elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                name = assignment_name(node)
                if name and name.isupper():
                    lines.append(f"{name} = {expression(node.value)}")
                    lines.append("")
    else:
        functions = {
            node.name: node
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        classes = {node.name: node for node in tree.body if isinstance(node, ast.ClassDef)}
        for name in public_members["functions"]:
            if name not in functions:
                raise SystemExit(f"public function not found: {module_name}.{name}")
            lines.extend(render_function(module_name, functions[name], ""))
            lines.append("")
        for name, methods in public_members["classes"].items():
            if name not in classes:
                raise SystemExit(f"public class not found: {module_name}.{name}")
            inherited_nodes = []
            descriptor = PUBLIC_INHERITED.get(module_name, {}).get(name)
            if descriptor:
                base_tree = ast.parse(
                    (repo_root / descriptor["source"]).read_text(encoding="utf-8"),
                    filename=descriptor["source"],
                )
                base_classes = {
                    node.name: node
                    for node in base_tree.body
                    if isinstance(node, ast.ClassDef)
                }
                base_class = base_classes.get(descriptor["class"])
                if base_class is None:
                    raise SystemExit(
                        f"inherited class not found: {module_name}.{name}: "
                        f"{descriptor['class']}"
                    )
                inherited_by_name = {
                    item.name: item
                    for item in base_class.body
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
                }
                for inherited_name in descriptor["methods"]:
                    if inherited_name not in inherited_by_name:
                        raise SystemExit(
                            f"inherited method not found: {module_name}.{name}: "
                            f"{inherited_name}"
                        )
                    inherited_nodes.append(inherited_by_name[inherited_name])
            lines.extend(
                render_class(module_name, classes[name], methods, tuple(inherited_nodes))
            )
            lines.append("")
        for alias_name, descriptor in PUBLIC_ALIASES.get(module_name, {}).items():
            alias_tree = ast.parse(
                (repo_root / descriptor["source"]).read_text(encoding="utf-8"),
                filename=descriptor["source"],
            )
            alias_classes = {
                node.name: node
                for node in alias_tree.body
                if isinstance(node, ast.ClassDef)
            }
            alias_class = alias_classes.get(descriptor["class"])
            if alias_class is None:
                raise SystemExit(
                    f"alias class not found: {module_name}.{alias_name}: "
                    f"{descriptor['class']}"
                )
            lines.extend(
                render_class(
                    module_name,
                    alias_class,
                    descriptor["methods"],
                    public_name=alias_name,
                )
            )
            lines.append("")
        local_constants = assignment_values(source)
        for name in public_members["constants"]:
            if name in local_constants:
                lines.append(f"{name} = {expression(local_constants[name])}")
                lines.append("")
        missing_constants = (
            set(public_members["constants"])
            - local_constants.keys()
            - PUBLIC_CONSTANTS.get(module_name, {}).keys()
        )
        if missing_constants:
            names = ", ".join(sorted(missing_constants))
            raise SystemExit(f"public constants not found: {module_name}: {names}")
    constant_values = {}
    for name, relative_source in PUBLIC_CONSTANTS.get(module_name, {}).items():
        if public_members is not None and name not in public_members["constants"]:
            continue
        if public_members is not None and name in local_constants:
            continue
        if relative_source not in constant_values:
            constant_values[relative_source] = assignment_values(
                repo_root / relative_source
            )
        values = constant_values[relative_source]
        if name not in values:
            raise SystemExit(f"public constant not found: {module_name}.{name}")
        lines.append(f"{name} = {expression(values[name])}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def output_files(repo_root: Path) -> dict[Path, str]:
    docs_root = repo_root / "ednex_docs"
    output_root = docs_root / "source" / "_api_stubs"
    result: dict[Path, str] = {}
    packages = {module.split(".")[0] for module in PUBLIC_MODULES if "." in module}
    for package in packages:
        result[output_root / package / "__init__.py"] = "# Generated package marker.\n"
    for module_name, relative_source in PUBLIC_MODULES.items():
        source = repo_root / relative_source
        if not source.is_file():
            raise SystemExit(f"source file not found: {source}")
        relative_module = Path(*module_name.split(".")).with_suffix(".py")
        result[output_root / relative_module] = render_module(module_name, source, repo_root)
    return result


def stale_output_files(output_root: Path, expected: dict[Path, str]) -> list[Path]:
    if not output_root.is_dir():
        return []
    expected_paths = set(expected)
    return sorted(
        path for path in output_root.rglob("*.py") if path not in expected_paths
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, help="firmware repository root")
    parser.add_argument("--check", action="store_true", help="check generated files without writing")
    args = parser.parse_args()
    repo_root = (args.repo_root or Path(__file__).resolve().parents[2]).resolve()
    expected = output_files(repo_root)
    mismatches = []
    for path, content in expected.items():
        actual = path.read_text(encoding="utf-8") if path.is_file() else None
        if actual != content:
            mismatches.append(path)
            if args.check and actual is not None:
                diff = difflib.unified_diff(actual.splitlines(), content.splitlines(), fromfile=str(path), tofile="generated")
                sys.stdout.writelines(line + "\n" for line in diff)
    output_root = repo_root / "ednex_docs" / "source" / "_api_stubs"
    stale = stale_output_files(output_root, expected)
    mismatches.extend(stale)
    if args.check:
        for path in stale:
            print(
                f"stale API stub: {path.relative_to(output_root)}",
                file=sys.stderr,
            )
        if mismatches:
            print("API stubs are out of date; run: make -C ednex_docs api-stubs", file=sys.stderr)
            return 1
        return 0
    for path in stale:
        path.unlink()
        print(f"removed stale API stub: {path.relative_to(output_root)}")
    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        # Avoid touching unchanged snapshots: sphinx-autobuild watches this
        # directory, so needless mtime changes would trigger rebuild loops.
        if path.is_file() and path.read_text(encoding="utf-8") == content:
            continue
        path.write_text(content, encoding="utf-8")
    print(
        f"generated {len(expected)} API stub files; "
        f"removed {len(stale)} stale API stub files"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
