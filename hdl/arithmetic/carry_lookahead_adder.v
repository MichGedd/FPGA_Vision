module carry_lookahead_adder #(parameter WIDTH=8) (input [WIDTH-1:0] x,
	input [WIDTH-1:0] y,
	input cin,
	output reg [WIDTH-1:0] sum,
	output reg cout);
	
	wire [WIDTH-1:0] sum_fa;
	wire [WIDTH-1:0] gen_fa;
	wire [WIDTH-1:0] prop_fa;
	wire [WIDTH:0] carry_cla;
	
	assign carry_cla[0] = cin;
	
	genvar i;
	
	generate
		for(i = 0; i < WIDTH; i = i + 1) begin : gen_full_adder
			full_adder fa (.x (x[i]),
				.y (y[i]),
				.cin (carry_cla[i]),
				.sum (sum_fa[i]),
				.cout (),
				.prop (prop_fa[i]),
				.gen (gen_fa[i]));
		end
		
		for(i = 0; i < WIDTH; i = i + 1) begin : gen_cla_logic
			assign carry_cla[i+1] = gen_fa[i] | (prop_fa[i] & carry_cla[i]);
		end
	
	endgenerate
	
	always @(*) begin
		sum <= sum_fa;
		cout <= carry_cla [WIDTH];
	end

endmodule
