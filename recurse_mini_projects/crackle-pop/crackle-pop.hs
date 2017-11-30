import Data.List

cracklePop :: Int -> String
cracklePop x =
  if (mod x 3 == 0) && (mod x 5 == 0)
    then "CracklePop"
    else if mod x 3 == 0
           then "Crackle"
           else if mod x 5 == 0
                  then "Pop"
                  else show x

main = putStrLn (intercalate " " (map cracklePop [1 .. 100]))
