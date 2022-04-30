module rgb_to_ycrcb(input clk,
	input [7:0] r,  // 8-bit unsigned
	input [7:0] g,  // 8-bit unsigned
	input [7:0] b,  // 8-bit unsigned
	output reg [7:0] y,  // 8-bit unsigned
	output reg [7:0] cr,  // 8-bit unsigned
	output reg [7:0] cb);  // 8-bit unsigned
	
	// Y constants
	wire [7:0] const_y_r = 8'h4c;  // 0.299 (actual is 0.296875)
	wire [7:0] const_y_g = 8'h96;  // 0.587 (actual is 0.5859375)
	wire [7:0] const_y_b = 8'h24;  // 0.144 (actual is0.140625)
	
	// Cr constants
	wire signed [8:0] const_cr_scale = 9'h0b6;  // 0.713 (actual is 0.7109375)
	
	// Cb constants
	wire signed [8:0] const_cb_scale = 8'h090;  // 0.564 (actual is 0.5625)
	
	// Obtain Y
	reg [15:0] y_product_r, y_product_g, y_product_b;
	
	always @(posedge clk) begin
		y_product_r <= r * const_y_r;
		y_product_g <= g * const_y_g;
		y_product_b <= b * const_y_b;
	end
	
	// Subtract Y from R and B
	wire signed [16:0] y_signed = y_product_r + y_product_g + y_product_b;
	reg signed [16:0] r_sub_y, b_sub_y;
	reg [8:0] y_buffer;
	
	always @(posedge clk) begin
		y_buffer <= y_signed[16:8];
		r_sub_y <= {1'b0, r, {8{1'b0}}} - y_signed;
		b_sub_y <= {1'b0, b, {8{1'b0}}} - y_signed;
	end
	
	// Multiply by Cr and Cb constants, fit to range (0-255)
	wire signed [24:0] cr_product =  r_sub_y * const_cr_scale + (128 << 16);
	wire signed [24:0] cb_product =  b_sub_y * const_cb_scale + (128 << 16);

	always @(posedge clk) begin
		cr <= cr_product[23:16];
		cb <= cb_product[23:16];
		
		if(y_buffer > 255) begin
			y <= 255;
		end else begin
			y <= y_buffer[7:0];
		end
	end
	
	
	
endmodule
