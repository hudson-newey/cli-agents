module Commands
  INBUILT_COMMANDS = {
    "/exit" => ->Command.exit,
  }

  def self.execute(command : String) : Void
    if command == "/exit" || command == "/close"
      Command.exit_session
    end
  end
end

private module Command
  def self.exit_session
    exit
  end
end
