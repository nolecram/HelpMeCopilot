  ****************************************************************
      *  This program demonstrates the following Language            *
      *  Environment callable                                        *
      *  services : CEEMOUT, CEELOCT, CEEDATE                        *
      ****************************************************************
      ****************************************************************
      **           I D          D I V I S I O N                    ***
      ****************************************************************
       Identification Division.
       Program-id.    AWIXMP.
      ****************************************************************
      **           D A T A      D I V I S I O N                    ***
      ****************************************************************
       Data Division.
       Working-Storage Section.
      ****************************************************************
      **  Declarations for the local date/time service.
      ****************************************************************
       01   Feedback.
       COPY CEEIGZCT
        02   Fb-severity      PIC 9(4) Binary.
        02   Fb-detail        PIC X(10).
       77   Dest-output       PIC S9(9) Binary.
       77   Lildate           PIC S9(9) Binary.
       77   Lilsecs           COMP-2.
       77   Greg              PIC X(17).
      ****************************************************************
      **  Declarations for messages and pattern for date formatting.
      ****************************************************************
       01   Pattern.
        02                    PIC 9(4) Binary Value 45.
        02                    PIC X(45) Value
            "Today is Wwwwwwwwwwwwz, Mmmmmmmmmmz ZD, YYYY.".

       77   Start-Msg         PIC X(80) Value
            "Callable Service example starting.".

       77   Ending-Msg        PIC X(80) Value
            "Callable Service example ending.".

       01 Msg.
         02 Stringlen         PIC S9(4) Binary.
         02 Str               .
          03                  PIC X Occurs 1 to 80 times
                                     Depending on Stringlen. 
      ****************************************************************
      **           P R O C      D I V I S I O N                    ***
      ****************************************************************
       Procedure Division.
       000-Main-Logic.
           Perform 100-Say-Hello.
           Perform 200-Get-Date.
           Perform 300-Say-Goodbye.
           Stop Run.
      **
      ** Setup initial values and say we are starting.
      **
       100-Say-Hello.
           Move 80 to Stringlen.
           Move 02 to Dest-output.
           Move Start-Msg to Str.
           CALL "CEEMOUT" Using Msg   Dest-output Feedback.
           Move Spaces to Str.        CALL "CEEMOUT" Using Msg Dest-output Feedback.
      **
      ** Get the local date and time and display it.
      **
       200-Get-Date.
           CALL "CEELOCT" Using Lildate Lilsecs     Greg      Feedback.
           CALL "CEEDATE" Using Lildate Pattern     Str       Feedback.
           CALL "CEEMOUT" Using Msg     Dest-output Feedback.
           Move Spaces to Str.
           CALL "CEEMOUT" Using Msg     Dest-output Feedback.
      **
      ** Say Goodbye.
      **
       300-Say-Goodbye.
           Move Ending-Msg to Str.
           CALL "CEEMOUT" Using Msg     Dest-output Feedback.
       End program AWIXMP.