module Main where

import Lib
import System.IO (isEOF)

import Data.List (group)
import Data.Map (Map, (!))
import qualified Data.Map as Map
import Debug.Trace

main :: IO ()
main = do
  contents <- getContents
  let ctlines = map words $ lines contents
  let withWeights = getWeights ctlines
  let withChildren = getChildren ctlines
  let children = concat $ map snd $ Map.toList withChildren
  let allNodes = map fst $ Map.toList withChildren
  let root = head $ filter (\n -> not $ elem n children) allNodes
  putStrLn $ show root
  let cumulativeWeights =
        buildCumulativeWeights root withWeights withChildren withWeights
  let unbalanced =
        findUnbalanced withWeights cumulativeWeights withChildren root
  putStrLn $ show unbalanced

getWeights :: [[String]] -> Map.Map String Int
getWeights contents = do
  let tplist =
        map
          (\line -> (head line, toInt $ removeChars "()" $ line !! 1))
          contents
  Map.fromList tplist

getChildren :: [[String]] -> Map.Map String [String]
getChildren contents = do
  let withChildren = filter (\l -> length l > 3) contents
  let tplist =
        map
          (\line ->
             (head line, map (removeChars ",") $ (tail . tail . tail) line))
          withChildren
  Map.fromList tplist

removeChars :: String -> String -> String
removeChars toRemove str = do
  filter (\c -> not $ elem c toRemove) str

toInt :: String -> Int
toInt = read

buildCumulativeWeights ::
     String
  -> Map.Map String Int
  -> Map.Map String [String]
  -> Map.Map String Int
  -> Map.Map String Int
buildCumulativeWeights current weights children acc = do
  let maybeChildren = Map.lookup current children
  case maybeChildren of
    Just curChildren -> do
      let acc' =
            foldl
              (\acc child -> buildCumulativeWeights child weights children acc)
              acc
              curChildren
      let childrensWeight = sum $ (acc' !) <$> curChildren
      let currentWeight = childrensWeight + (weights ! current)
      Map.insert current currentWeight acc'
    Nothing -> acc

unbalanced :: Map.Map String Int -> Map.Map String [String] -> String -> Bool
unbalanced cumulativeWeights children current = do
  case Map.lookup current children of
    Nothing -> False
    Just curChildren -> do
      let childCWeights = (cumulativeWeights !) <$> curChildren
      let weightGroups = Data.List.group $ childCWeights
      1 < (length weightGroups)

findUnbalanced ::
     Map.Map String Int
  -> Map.Map String Int
  -> Map.Map String [String]
  -> String
  -> Maybe Int
findUnbalanced weights cumulativeWeights children current = do
  case Map.lookup current children of
    Nothing -> Nothing
    Just curChildren -> do
      let childCWeights = (cumulativeWeights !) <$> curChildren
      let weightGroups = Data.List.group $ childCWeights
      if 1 < (length weightGroups)
        then do
          let unbalancedSon =
                filter (unbalanced cumulativeWeights children) curChildren
          if not $ null unbalancedSon
            then findUnbalanced
                   weights
                   cumulativeWeights
                   children
                   (head unbalancedSon)
            else do
              let shouldCWeight =
                    head $ head $ filter (\x -> (length x) > 1) weightGroups
              let outlierCWeight =
                    head $ filter (/= shouldCWeight) childCWeights
              let outlier =
                    traceShowId $
                    head $
                    filter
                      (\c -> (cumulativeWeights ! c) == outlierCWeight)
                      curChildren
              let outlierWeight = weights ! outlier
              Just $ outlierWeight + shouldCWeight - outlierCWeight
        else Nothing
