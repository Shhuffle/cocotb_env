module FIFO (
    input  logic clk,rst,wr_en,rd_en,
    input  logic [7:0] din,
    output logic full, empty,
    output logic [7:0] dout
);
    logic [7:0] mem[0:1024];
    logic [15:0] count;

    parameter one_kb = 10'd1024;
    assign empty = (!count) ? 1'b1 : 1'b0;
    assign full =  (count == one_kb) ? 1'b1 : 1'b0;

    logic [15:0] wr_ptr , rd_ptr ;


    always_ff @(posedge clk or negedge rst) begin 
        if(!rst) begin 
            foreach (mem[i]) begin
                mem[i] <= 8'b0;
            end
            count <= 10'b0;
            wr_ptr <= 15'b0;
            rd_ptr <= 15'b0;

        end else if(rst) begin 
            if(wr_en && !full) begin 
                mem[wr_ptr] <= din;
                wr_ptr <= wr_ptr + 1;
                            
            end

        end
    end

endmodule