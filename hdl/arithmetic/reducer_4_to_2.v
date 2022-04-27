module reducer_4_to_2 #(parameter WIDTH=8) (input [WIDTH-1:0] w,
	input [WIDTH-1:0] x,
	input [WIDTH-1:0] y,
	input [WIDTH-1:0] z,
	input cin,
	output reg [WIDTH-1:0] sum,
	output reg [WIDTH-1:0] carry,
	output reg cout);
	
	reg [WIDTH:0] carries;
	
	integer i;
	
	always @(*) begin
		
		carries[0] = cin;
	
		for(i = 0; i < WIDTH; i = i + 1) begin
			sum[i] = w[i] ^ x[i] ^ y[i] ^ z[i] ^ carries[i];
			carries[i+1] = (w[i] & x[i]) | (y[i] & z[i]) | (x[i] & z[i]) | (w[i] & z[i]) | (w[i] & y[i]) | (x[i] & z[i]);
			carry[i] = (w[i] & x[i] & y[i] & z[i]) | (carries[i] & !sum[i]);
		end
		
		cout = carries[WIDTH];
	end

endmodule

