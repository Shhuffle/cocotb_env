module FIFO (
    input  logic clk,rst,wr_en,rd_en,
    input  logic [7:0] din,
    output logic full, empty,
    output bit [7:0] dout
);
    logic [7:0] mem[0:1023];
    logic [15:0] count;

    parameter one_kb = 10'd1024;
    empty = (!count) ? 1'b1 : 1'b0;
    full =  (count == one_kb) ? 1'b1 : 1'b0;

    logic [15:0] wr_ptr , rd_ptr ;


    always_ff @(posedge clk or negedge rst) begin 
        if(!rst) begin 
            foreach (mem[i]) begin
                mem[i] <= 8'b0;
            end
            count <= 16'b0;
            wr_ptr <= 16'b0;
            rd_ptr <= 16'b0;
            empty <= 1'b0;
            full <= 1'b0;

        end else if(rst) begin 
            if(wr_en && !full) begin 
                mem[wr_ptr] <= din;
                if(wr_ptr == 16'd1023)
                    wr_ptr <= 16'b0;
                else  
                    wr_ptr <= wr_ptr + 1;

                count <= count + 1;              
            end
            
            if(rd_en && !empty) begin 
                dout <= mem[rd_ptr];
                if(rd_ptr == 16'd1023)
                    rd_ptr <= 16'b0; 
                else 
                    rd_ptr <= rd_ptr + 1;                                            
            end
            if(!rd_en) begin 
                dout <= 8'b0;
                
            end
        end
    end
endmodule