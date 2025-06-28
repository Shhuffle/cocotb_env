module FIFO (
    input  logic clk,rst,wr_en,rd_en,
    input  logic [7:0] din,
    output logic full, empty,
    output logic [7:0] dout
);
    logic [7:0] mem[0:1023];
    logic [15:0] count;

    parameter one_kb = 10'd1023;
    assign empty = (!count) ? 1'b1 : 1'b0;
    assign full =  (count == one_kb) ? 1'b1 : 1'b0;

    logic [15:0] wr_ptr , rd_ptr ;


    always_ff @(posedge clk or negedge rst) begin 
        if(!rst) begin 
            foreach (mem[i]) begin
                mem[i] <= 8'b0;
            end
            count <= 16'b0;
            wr_ptr <= 16'b0;
            rd_ptr <= 16'b0;
            dout <= 8'bz; //Buffer in high impedance after each reset.
            $display("Inside rst"); //for debugginf purpose
            

        end else if(rst) begin 
            //Write Operation
            if(wr_en && !full) begin 
                $display("Inside write"); //for debugginf purpose
                mem[wr_ptr] <= din;
                if(wr_ptr == 16'd1023)
                    wr_ptr <= 16'b0;
                else  
                    wr_ptr <= wr_ptr + 1;

                count <= count + 1;              
            end
            
            //Read Operation
            if(rd_en && !empty) begin 
                $display("Inside read");  //for debugginf purpose
                dout <= mem[rd_ptr];
                mem[rd_ptr] <= 8'b0;
                if(rd_ptr == 16'd1023)
                    rd_ptr <= 16'b0; 
                else 
                    rd_ptr <= rd_ptr + 1;                                            
            end
            if(!rd_en) begin 
                dout <= 8'bz; //if the buffer is not in the read mode then the output of the buffer should be in high impedance
            end
        end
    end
endmodule