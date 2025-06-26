module ALU(input logic [1:0] SEL, 
            input bit clk , rst,
            input logic [7:0] a , b ,
            output logic [7:0]y
            );
            logic [7:0] out;

        always_ff @(posedge clk) begin
            if(!rst) begin 
                out <= 8'b0;
            end
            else begin 
                case(SEL) 
                    2'b00 :  out <= a * b;
                    2'b01 :  out <= (b != 0) ? (a / b) : 8'b0;
                    2'b10 :  out <= a+b;
                    2'b11 :  out <= a-b;
                endcase
            end
        end
        assign y = out;
endmodule