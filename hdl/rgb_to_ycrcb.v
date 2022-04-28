module rgb_to_ycrcb(input clk,
	input [7:0] r,  // 8-bit unsigned
	input [7:0] g,  // 8-bit unsigned
	input [7:0] b,  // 8-bit unsigned
	output reg [7:0] y,  // 8-bit unsigned
	output reg [7:0] cr,  // 8-bit unsigned
	output reg [7:0] cb);  // 8-bit unsigned
	
	// Y constants
	wire [7:0] const_y_r = 8'h4c;  // 0.299
	wire [7:0] const_y_g = 8'h96;  // 0.587
	wire [7:0] const_y_b = 8'h24;  // 0.144
	
	// Cr constants
	wire [7:0] const_cr_scale = 8'hb6;  // 0.713
	
	// Cb constants
	wire [7:0] const_cb_scale = 8'h90;  // 0.564
	
	// Multiply
	reg [15:0] y_product_r, y_product_g, y_product_b;
	
	always @(posedge clk) begin
		y_product_r <= r * const_y_r;
		y_product_g <= g * const_y_g;
		y_product_b <= b * const_y_b;
	end
	
	// Add
	wire signed [16:0] y_signed = y_product_r + y_product_g + y_product_b;
	reg signed [16:0] r_sub_y, b_sub_y;
	reg [7:0] y_buffer;
	
	always @(posedge clk) begin
		y_buffer <= y_signed[15:8];
		r_sub_y <= {1'b0, r, {8{1'b0}}} - y_signed;
		b_sub_y <= {1'b0, b, {8{1'b0}}} - y_signed;
	end
	
	
endmodule
