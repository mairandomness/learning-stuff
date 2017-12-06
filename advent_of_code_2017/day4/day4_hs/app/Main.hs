module Main where

import Data.Char
import Data.List
import Lib
import System.IO (isEOF)

main :: IO ()
main = do
  contents <- getContents
  let passphrases = lines contents
  let validPassphrases = filter isValid passphrases
  putStrLn $ show $ length validPassphrases
  let validNoAnagrams = filter isValidNoAnagrams passphrases
  putStrLn $ show $ length validNoAnagrams

isValid :: String -> Bool
isValid pass = do
  let passWords = words pass
  let equals = [a | a <- passWords, b <- passWords, a == b]
  equals == passWords

isValidNoAnagrams :: String -> Bool
isValidNoAnagrams pass = do
  let passWords = words pass
  let sortedPassWords = map sort passWords
  isValid $ unwords sortedPassWords
