require "./agent"
require "./commands"

class UI
  def enter
    agent = Agent.new

    while true
      print "> "
      user_input : String = gets.not_nil!.chomp

      Commands.execute user_input

      agent.send user_input
    end
  end
end
