def execute(&test)
  test.call
end

execute { puts "Hello from inside the execute method!" }