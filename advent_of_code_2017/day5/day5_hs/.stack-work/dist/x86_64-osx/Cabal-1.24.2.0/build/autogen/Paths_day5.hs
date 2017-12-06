{-# LANGUAGE CPP #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
{-# OPTIONS_GHC -fno-warn-implicit-prelude #-}
module Paths_day5 (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/Users/juliano/git/advent_of_code/day5/.stack-work/install/x86_64-osx/lts-9.17/8.0.2/bin"
libdir     = "/Users/juliano/git/advent_of_code/day5/.stack-work/install/x86_64-osx/lts-9.17/8.0.2/lib/x86_64-osx-ghc-8.0.2/day5-0.1.0.0-4MUoJVhhsPMKLk67rrIOFR"
dynlibdir  = "/Users/juliano/git/advent_of_code/day5/.stack-work/install/x86_64-osx/lts-9.17/8.0.2/lib/x86_64-osx-ghc-8.0.2"
datadir    = "/Users/juliano/git/advent_of_code/day5/.stack-work/install/x86_64-osx/lts-9.17/8.0.2/share/x86_64-osx-ghc-8.0.2/day5-0.1.0.0"
libexecdir = "/Users/juliano/git/advent_of_code/day5/.stack-work/install/x86_64-osx/lts-9.17/8.0.2/libexec"
sysconfdir = "/Users/juliano/git/advent_of_code/day5/.stack-work/install/x86_64-osx/lts-9.17/8.0.2/etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "day5_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "day5_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "day5_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "day5_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "day5_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "day5_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
