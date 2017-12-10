module Main where

import System.IO (isEOF)

main :: IO ()
main = do
  contents <- getContents
  let total = parse False 0 contents 0
  let total2 = parse2 False contents 0
  putStrLn $ show total
  putStrLn $ show total2

parse :: Bool -> Int -> String -> Int -> Int
parse False lvl ('{':t) total = parse False (lvl + 1) t total
parse False lvl ('}':t) total = parse False (lvl - 1) t (total + lvl)
parse False lvl ('<':t) total = parse True lvl t total
parse True lvl ('>':t) total = parse False lvl t total
parse True lvl ('!':t) total = parse True lvl (tail t) total
parse _ _ [] total = total
parse garbage lvl (_:t) total = parse garbage lvl t total

parse2 :: Bool -> String -> Int -> Int
parse2 False ('<':t) total = parse2 True t total
parse2 True ('>':t) total = parse2 False t total
parse2 True ('!':t) total = parse2 True (tail t) total
parse2 True (_:t) total = parse2 True t (total + 1)
parse2 _ [] total = total
parse2 garbage (_:t) total = parse2 garbage t total
