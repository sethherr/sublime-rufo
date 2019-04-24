import os
import fnmatch
import subprocess
import sublime
import sublime_plugin


class RufoPluginListener(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    view.run_command("rufo")

class RufoCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    window = self.view.window()
    filename = self.view.file_name()
    # I was initially thinking of running the command from the project root, but I think that could introduce bugs
    # Instead, just use the folder of the file
    project_variables = window.extract_variables()
    command_dir = project_variables["file_path"]
    filename_matchers = ["*.rb", "*.rake", "*gemfile"]
    # Check if the current filename matches any of our filname matcher globs
    if any(fnmatch.fnmatch(filename.lower(), glob) for glob in filename_matchers):
      print("Matching filename")
      os.chdir(command_dir)
      command = "bundle exec rufo '" + filename + "'"
      print(command, command_dir)
      print(subprocess.check_output("ruby --version", shell = True))
      # subprocess.check_call('rvm env --path -- ruby-version[@gemset-name]')
      # output = subprocess.check_output(command, shell = True)

      # vsize = self.view.size()
      # region = sublime.Region(0, vsize)
      # src = self.view.substr(region)
      # with subprocess.Popen("rufo", stdin = subprocess.PIPE, stdout = subprocess.PIPE, shell = True) as proc:
      #   proc.stdin.write(bytes(src, "UTF-8"))
      #   proc.stdin.close()
      #   output = proc.stdout.read().decode("UTF-8")
      #   exit = proc.wait()

      # pos = 0
      # print(exit)
      # print(output)
      # if exit == 3:
      #   print("FFFFFF")
      #   if not self.has_redo():
      #     for op, text in diff_match_patch().diff_main(src, output):
      #       if op == diff_match_patch.DIFF_DELETE:
      #         self.view.erase(edit, sublime.Region(pos, pos + len(text)))
      #       if op == diff_match_patch.DIFF_INSERT:
      #         self.view.insert(edit, pos, text)
      #         pos += len(text)
      #       if op == diff_match_patch.DIFF_EQUAL:
      #         pos += len(text)

      # output = subprocess.Popen(cmd, shell = True)
      # proc.stdin.write(bytes(src, "UTF-8"))
      # proc.stdin.close()
      # output = proc.stdout.read().decode("UTF-8")
      # exit = proc.wait()
      print("Ran it")
    else:
      print("non-matching filename")
    # print(fnmatch.fnmatch(filename.lower(), "*.rb"))
    # if self.parseFilename("'" + filename + "'"):
    # print("We're parsing!")
    # For simplicity, just running the command in the folder of the file that was saved
    # command_dir = self.view.filename
    # command = [rufo_cmd, "--filename", filename]
    # caret = self.view.sel()[0].a
    # msg = self.view.scope_name(caret)
    # msg = "'Hello, World!'\n"

    # project_data = sublime.Window.project_data(self)

    # sublime.error_message(msg)
    # os.chdir()
    # print(project_variables)

    # print(command_dir)
    print()