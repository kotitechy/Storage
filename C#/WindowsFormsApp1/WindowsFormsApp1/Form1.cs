using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void label7_Click(object sender, EventArgs e)
        {




        }
        private void subs(object sender, EventArgs e)
        {
            string s =  textBox2.Text;
            string s1 = textBox3.Text;
            string s2 = textBox4.Text;
            DateTime dt = dateTimePicker1.Value;
            if (MALE.Checked)
            {
                MessageBox.Show("gender : male");
            }
            else if (radioButton2.Checked)
            {
                MessageBox.Show("gender : female");
            }
            MessageBox.Show("name: " + s1);
            MessageBox.Show("mobile no: " + s);
            MessageBox.Show("pin no: " + s2);
            MessageBox.Show("date : " + dt);
        }
        private void cs(object sender, EventArgs e)
        {
            OpenFileDialog op = new OpenFileDialog();
            if (op.ShowDialog() == DialogResult.OK)
            {
                string im= op.FileName;
                MessageBox.Show("photo: " + im);
               pictureBox1.Image=Image.FromFile(im);
                byte[] imbytes = File.ReadAllBytes(im);
                MessageBox.Show("binary data : ");
                foreach(byte b in imbytes)
                {
                    Console.WriteLine("${ b:x2}");
                }

            }
            else
            {
                MessageBox.Show("error: " );
            }
        }
        }
}
