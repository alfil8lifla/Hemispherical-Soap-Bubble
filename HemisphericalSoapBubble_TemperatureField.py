{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red183\green111\blue179;\red23\green23\blue23;\red202\green202\blue202;
\red167\green197\blue152;\red89\green156\blue62;\red70\green137\blue204;\red212\green214\blue154;\red140\green211\blue254;
\red212\green212\blue212;\red194\green126\blue101;}
{\*\expandedcolortbl;;\cssrgb\c77255\c52549\c75294;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c70980\c80784\c65882;\cssrgb\c41569\c66275\c30980;\cssrgb\c33725\c61176\c83922;\cssrgb\c86275\c86275\c66667;\cssrgb\c61176\c86275\c99608;
\cssrgb\c86275\c86275\c86275;\cssrgb\c80784\c56863\c47059;}
\margl1440\margr1440\vieww19440\viewh16100\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  numpy \cf2 \strokec2 as\cf4 \strokec4  np\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  matplotlib.pyplot \cf2 \strokec2 as\cf4 \strokec4  plt\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 n = \cf5 \strokec5 2\cf4 \strokec4           \cf6 \strokec6 # Period=2\uc0\u960 /n\cf4 \cb1 \strokec4 \
\cb3 epsilon = \cf5 \strokec5 0.1\cf4 \strokec4   \cf6 \strokec6 # Amplitude of the small sinusoidal thermal fluctuation at the equatorial region\cf4 \cb1 \strokec4 \
\
\cb3 phi_0 = np.pi / \cf5 \strokec5 500\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf8 \strokec8 coth\cf4 \strokec4 (\cf9 \strokec9 x\cf4 \strokec4 )\cf10 \strokec10 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 return\cf4 \strokec4  np.cosh\cf10 \strokec10 (\cf4 \strokec4 x\cf10 \strokec10 )\cf4 \strokec4  / np.sinh\cf10 \strokec10 (\cf4 \strokec4 x\cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf8 \strokec8 cot\cf4 \strokec4 (\cf9 \strokec9 x\cf4 \strokec4 )\cf10 \strokec10 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 return\cf4 \strokec4  np.cos\cf10 \strokec10 (\cf4 \strokec4 x\cf10 \strokec10 )\cf4 \strokec4  / np.sin\cf10 \strokec10 (\cf4 \strokec4 x\cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf8 \strokec8 T\cf4 \strokec4 (\cf9 \strokec9 theta\cf4 \strokec4 , \cf9 \strokec9 phi\cf4 \strokec4 , \cf9 \strokec9 epsilon\cf4 \strokec4 =epsilon, \cf9 \strokec9 n\cf4 \strokec4 =n)\cf10 \strokec10 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf10 \strokec10 (\cf5 \strokec5 1\cf4 \strokec4  + epsilon * np.sin\cf10 \strokec10 (\cf4 \strokec4 n * theta\cf10 \strokec10 ))\cf4 \strokec4  * \cf10 \strokec10 (\cf4 \cb1 \strokec4 \
\cb3         np.cosh\cf10 \strokec10 (\cf4 \strokec4 n * np.arctanh\cf10 \strokec10 (\cf4 \strokec4 np.cos\cf10 \strokec10 (\cf4 \strokec4 phi\cf10 \strokec10 )))\cf4 \strokec4  -\cb1 \
\cb3         coth\cf10 \strokec10 (\cf4 \strokec4 n*np.log\cf10 \strokec10 (\cf4 \strokec4 cot\cf10 \strokec10 (\cf4 \strokec4 phi_0\cf10 \strokec10 )))\cf4 \strokec4  * np.sinh\cf10 \strokec10 (\cf4 \strokec4 n * np.arctanh\cf10 \strokec10 (\cf4 \strokec4 np.cos\cf10 \strokec10 (\cf4 \strokec4 phi\cf10 \strokec10 )))\cf4 \cb1 \strokec4 \
\cb3     \cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\
\cb3 theta_vals = np.linspace\cf10 \strokec10 (\cf5 \strokec5 0\cf10 \strokec10 ,\cf4 \strokec4  \cf5 \strokec5 2\cf4 \strokec4  * np.pi\cf10 \strokec10 ,\cf4 \strokec4  \cf5 \strokec5 200\cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\cb3 phi_vals = np.linspace\cf10 \strokec10 (\cf4 \strokec4 phi_0\cf10 \strokec10 ,\cf4 \strokec4  np.pi / \cf5 \strokec5 2\cf10 \strokec10 ,\cf4 \strokec4  \cf5 \strokec5 200\cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\cb3 Theta\cf10 \strokec10 ,\cf4 \strokec4  Phi = np.meshgrid\cf10 \strokec10 (\cf4 \strokec4 theta_vals\cf10 \strokec10 ,\cf4 \strokec4  phi_vals\cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\
\cb3 T_vals = T\cf10 \strokec10 (\cf4 \strokec4 Theta\cf10 \strokec10 ,\cf4 \strokec4  Phi\cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\
\cb3 plt.figure\cf10 \strokec10 (\cf4 \strokec4 figsize=\cf10 \strokec10 (\cf5 \strokec5 8\cf10 \strokec10 ,\cf4 \strokec4  \cf5 \strokec5 7\cf10 \strokec10 ))\cf4 \cb1 \strokec4 \
\cb3 c = plt.contourf\cf10 \strokec10 (\cf4 \strokec4 Theta\cf10 \strokec10 ,\cf4 \strokec4  Phi\cf10 \strokec10 ,\cf4 \strokec4  T_vals\cf10 \strokec10 ,\cf4 \strokec4  levels=\cf5 \strokec5 50\cf10 \strokec10 ,\cf4 \strokec4  cmap=\cf11 \strokec11 "coolwarm"\cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\cb3 plt.xlabel\cf10 \strokec10 (\cf11 \strokec11 "
\f1 \uc0\u952 
\f0 "\cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\cb3 plt.ylabel\cf10 \strokec10 (\cf11 \strokec11 "$\\Phi$"\cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\cb3 plt.xticks\cf10 \strokec10 ([\cf5 \strokec5 0\cf10 \strokec10 ,\cf4 \strokec4  np.pi/\cf5 \strokec5 2\cf10 \strokec10 ,\cf4 \strokec4  np.pi\cf10 \strokec10 ,\cf4 \strokec4  \cf5 \strokec5 3\cf4 \strokec4 *np.pi/\cf5 \strokec5 2\cf10 \strokec10 ,\cf4 \strokec4  \cf5 \strokec5 2\cf4 \strokec4 *np.pi\cf10 \strokec10 ],\cf4 \strokec4  \cf10 \strokec10 [\cf11 \strokec11 "0"\cf10 \strokec10 ,\cf4 \strokec4  \cf11 \strokec11 "\uc0\u960 /2"\cf10 \strokec10 ,\cf4 \strokec4  \cf11 \strokec11 "\uc0\u960 "\cf10 \strokec10 ,\cf4 \strokec4  \cf11 \strokec11 "3\uc0\u960 /2"\cf10 \strokec10 ,\cf4 \strokec4  \cf11 \strokec11 "2\uc0\u960 "\cf10 \strokec10 ])\cf4 \cb1 \strokec4 \
\cb3 plt.yticks\cf10 \strokec10 ([\cf5 \strokec5 0\cf10 \strokec10 ,\cf4 \strokec4  np.pi/\cf5 \strokec5 4\cf10 \strokec10 ,\cf4 \strokec4  np.pi/\cf5 \strokec5 2\cf10 \strokec10 ],\cf4 \strokec4  \cf10 \strokec10 [\cf11 \strokec11 "0"\cf10 \strokec10 ,\cf4 \strokec4  \cf11 \strokec11 "\uc0\u960 /4"\cf10 \strokec10 ,\cf4 \strokec4  \cf11 \strokec11 "\uc0\u960 /2"\cf10 \strokec10 ])\cf4 \cb1 \strokec4 \
\cb3 plt.title\cf10 \strokec10 (\cf11 \strokec11 "Contour Plot de T(
\f1 \uc0\u952 
\f0 , $\\Phi$)"\cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\cb3 plt.gca\cf10 \strokec10 ()\cf4 \strokec4 .invert_yaxis\cf10 \strokec10 ()\cf4 \cb1 \strokec4 \
\cb3 plt.show\cf10 \strokec10 ()\cf4 \cb1 \strokec4 \
}