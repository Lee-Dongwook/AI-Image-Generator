import importlib.util
import platform
from importlib.metadata import version
import launch
from packaging.version import parse


def is_installed(package: str):
    min_version = "0.0.0"
    max_version = "99999999.99999999.99999999"
    pkg_name = package
    version_check = True
    if "==" in package:
        pkg_name, _version = package.split("==")
        min_version = max_version = _version
    elif "<=" in package:
        pkg_name, _version = package.split("<=")
        max_version = _version
    elif ">=" in package:
        pkg_name, _version = package.split(">=")
        min_version = _version
    else:
        version_check = False
    package = pkg_name
    try:
        spec = importlib.util.find_spec(package)
    except ModuleNotFoundError:
        message = f"is_installed check for {str(package)} failed as error ModuleNotFoundError"
        print(message)
        return False
    if spec is None:
        message = f"is_installed check for {str(package)} failed as 'spec is None'"
        print(message)
        return False
    if not version_check:
        return True
    if package == "google.protobuf":
        package = "protobuf"
    try:
        pkg_version = version(package)
        return parse(min_version) <= parse(pkg_version) <= parse(max_version)
    except Exception as e:
        message = f"is_installed check for {str(package)} failed as error {str(e)}"
        print(message)
        return False



if not is_installed("cv2"):
    print("Installing requirements for easyphoto-webui")
    launch.run_pip("install opencv-python", "requirements for opencv")

if not is_installed("tensorflow-cpu"):
    print("Installing requirements for easyphoto-webui")
    launch.run_pip("install tensorflow-cpu", "requirements for tensorflow")

if not is_installed("onnx"):
    print("Installing requirements for easyphoto-webui")
    launch.run_pip("install onnx", "requirements for onnx")

if not is_installed("onnxruntime"):
    print("Installing requirements for easyphoto-webui")
    launch.run_pip("install onnxruntime", "requirements for onnxruntime")

if not is_installed("modelscope==1.9.3"):
    print("Installing requirements for easyphoto-webui")
    launch.run_pip("install modelscope==1.9.3", "requirements for modelscope")

if not is_installed("einops"):
    print("Installing requirements for easyphoto-webui")
    launch.run_pip("install einops", "requirements for diffusers")

if not is_installed("imageio>=2.29.0"):
    print("Installing requirements for easyphoto-webui")
    launch.run_pip("install \"imageio>=2.29.0\"", "requirements for imageio")

if not is_installed("av"):
    print("Installing requirements for easyphoto-webui")
    launch.run_pip("install \"imageio[pyav]\"", "requirements for av")

if not is_installed("fsspec==2023.9.2"):
    print("Installing requirements for easyphoto-webui")
    launch.run_pip("install fsspec==2023.9.2", "requirements for fsspec")

if not launch.is_installed("invisible-watermark"):
    print("Installing requirements for easyphoto-webui")
    launch.run_pip("install invisible-watermark", "requirements for invisible-watermark")

if not launch.is_installed("shapely"):
    print("Installing requirements for easyphoto-webui")
    launch.run_pip("install shapely", "requirements for shapely")

if not launch.is_installed("segment_anything"):
    try:
        launch.run_pip("install segment-anything", "requirements for segment_anything")
    except Exception:
        print("Can't install segment-anything. Please follow the readme to install manually")

if not is_installed("diffusers>=0.18.2"):
    print("Installing requirements for easyphoto-webui")
    try:
        launch.run_pip("install diffusers==0.23.0", "requirements for diffusers")
    except Exception as e:
        print(f"Can't install the diffusers==0.23.0. Error info {e}")
        launch.run_pip("install diffusers==0.18.2", "requirements for diffusers")

if platform.system() != "Windows":
    if not is_installed("nvitop"):
        print("Installing requirements for easyphoto-webui")
        launch.run_pip("install nvitop==1.3.0", "requirements for tensorflow")