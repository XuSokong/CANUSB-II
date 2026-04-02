program Project1;

uses
  Forms,
  Unit1 in 'Unit1.pas' {Form1},
  CAN_TO_USB in 'CAN_TO_USB.pas';

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.Run;
end.
