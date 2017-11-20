#! /bin/bash
mv ~/Library/Developer/Xcode/UserData/CodeSnippets ~/Library/Developer/Xcode/UserData/CodeSnippets.backup

# rm ~/Library/Developer/Xcode/UserData/CodeSnippets

SRC_HOME=`pwd`
ln -s ~/Documents/gworkspace/MyCodeSnippet/CodeSnippets ~/Library/Developer/Xcode/UserData/CodeSnippets
echo "done"

