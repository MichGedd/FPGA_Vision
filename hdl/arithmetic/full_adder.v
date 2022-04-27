module full_adder (input x, input y, input cin, output reg sum, output reg cout, output reg prop, output reg gen);
	
	always @(*) begin
		sum <= x ^ y ^ cin;
		cout <= ((x ^ y) & cin) | (x & y);
		prop <= x ^ y;
		gen <= x & y;
	end
	
endmodule
