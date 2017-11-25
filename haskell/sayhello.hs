--just a silly function used to understand how to
--load files to repl and use functions there
sayHello :: String -> IO ()
sayHello x =
  putStrLn ("Hello, " ++ x ++ "!")
