gametextcompiler.exe ^
LOAD_MULTI_STR(FILE_ID:0,FILE_PATH:generals_multi.str,LANGUAGE:All) ^
LOAD_STR(FILE_ID:1,FILE_PATH:generals_german.str) ^
SWAP_AND_SET_LANGUAGE(FILE_ID:1,LANGUAGE:German) ^
MERGE_AND_OVERWRITE(FILE_ID:0,FILE_ID:1,LANGUAGE:German) ^
SAVE_MULTI_STR(FILE_ID:0,FILE_PATH:generals_new.str,LANGUAGE:English^|German^|French^|Spanish^|Italian^|Korean^|Chinese^|Brazilian^|Polish^|Russian^|Arabic)
