import os
import sys
import subprocess


py_pkgs = os.path.join(os.path.dirname(__file__), 'py-pkgs')
os.makedirs(py_pkgs, exist_ok=True)
sys.path.append(py_pkgs)

os.environ['PYTHONPATH'] = py_pkgs+os.pathsep+os.environ.get('PYTHONPATH', '')

try:
  import marimo
except:
  subprocess.run([
    sys.executable, '-m', 'pip', 'install', f'--target={py_pkgs}', 'marimo'
  ])
  import marimo

if __name__ == '__main__':
  notebook_script_file = os.path.abspath(sys.argv[1])
  notebook_script_venv = os.path.join(
    os.path.dirname(notebook_script_file),
    os.path.basename(notebook_script_file).replace('.py', '').replace('.', '_')+'-venv'
  )

  if not os.path.exists(notebook_script_venv):
    subprocess.run([
      sys.executable, '-m', 'venv', notebook_script_venv
    ], check=True)

  if 'PYTHONHOME' in os.environ:
    os.environ.pop('PYTHONHOME')

  os.environ['PATH'] = os.path.join(notebook_script_venv, 'bin')+os.pathsep+os.environ.get('PATH', '')
  os.environ['VIRTUAL_ENV'] = notebook_script_venv
  os.environ['VIRTUAL_ENV_PROMPT'] = f'({os.path.basename(notebook_script_file)}) '

  os.environ['PYTHONUSERBASE'] = notebook_script_venv

  subprocess.run([
    os.path.join(notebook_script_venv, 'bin', 'python'), '-m', 'marimo', 'edit', notebook_script_file
  ])


