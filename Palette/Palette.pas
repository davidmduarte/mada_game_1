program Palette;

uses raylib;

const
	SIZE = 48;
	SIZE2 = 16;
var
	i, j: Integer;
	x, y: Integer;
	aux: Integer;
	state: Integer;
	plt: array[0..SIZE2, 0..SIZE] of TColorB;
begin
	state := 1;
	aux := 0;
	plt[0, 0].r := 255;
	plt[0, 0].g := 0;
	plt[0, 0].b := 0;
	plt[0, 0].a := 255;
	for j := 1 to SIZE do begin
		if j > 0 then begin
			plt[0, j].r := plt[0, j - 1].r;
			plt[0, j].g := plt[0, j - 1].g;
			plt[0, j].b := plt[0, j - 1].b;
			plt[0, j].a := 255;
		end;
		case state of
			1:	begin
					aux := aux + 32;
					if aux >= 255 then begin
						plt[0, j].g := 255;
						state := 2;
						aux := 255;
					end else plt[0, j].g := aux;
				end;
			2:	begin
					aux := aux - 32;
					if aux <= 0 then begin
						plt[0, j].r := 0;
						state := 3;
						aux := 0;
					end else plt[0, j].r := aux;		
				end;
			3:	begin
					aux := aux + 32;
					if aux >= 255 then begin
						plt[0, j].b := 255;
						state := 4;
						aux := 255;
					end else plt[0, j].b := aux;
				end;
			4:	begin
					aux := aux - 32;
					if aux <= 0 then begin
						plt[0, j].g := 0;
						state := 5;
						aux := 0;
					end else plt[0, j].g := aux;		
				end;
			5: 	begin
					aux := aux + 32;
					if aux >= 255 then begin
						plt[0, j].r := 255;
						state := 6;
						aux := 0;
					end else plt[0, j].r := aux;
				end;
			6: 	begin
					aux := aux + 32;
					if aux >= 255 then begin
						plt[0, j].g := 255;
						state := 1;
						aux := 0;
					end else plt[0, j].g := aux;
				end;
		end;
	end;

	for i := 1 to SIZE2 do begin
		for j := 0 to SIZE do begin
			if plt[i - 1, j].r < 16 then plt[i, j].r := 0
			else plt[i, j].r := plt[i - 1, j].r - 16;
			
			if plt[i - 1, j].g < 16 then plt[i, j].g := 0
			else plt[i, j].g := plt[i - 1, j].g - 16;

			if plt[i - 1, j].b < 16 then plt[i, j].b := 0
			else plt[i, j].b := plt[i - 1, j].b - 16;

			plt[i, j].a := 255;
		end;
	end;

	writeln('r:', plt[0, 0].r, ' g:', plt[0, 0].g, ' b:', plt[0, 0].b);
	writeln('r:', plt[1, 0].r, ' g:', plt[1, 0].g, ' b:', plt[1, 0].b);

	InitWindow(598, 200, 'Palette');
	SetTargetFps(60);

	while not WindowShouldClose() do begin
		BeginDrawing();

		for i := 0 to SIZE2 do begin
			y := i * 12;
			for j := 0 to SIZE do begin
				x := j * 12;
				DrawRectangle(x+6, y+4, 10, 10, plt[i, j]);
			end;
		end;
		
		EndDrawing();
	end;
	
	CloseWindow();
end.
