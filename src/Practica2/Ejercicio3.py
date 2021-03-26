lorem = """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
Exercitationem quam obcaecati ducimus rerum facere tenetur reiciendis iste minima! 
Maiores, deleniti fuga. Odio quo natus accusamus ullam nam, vel 
facere delectus labore ipsam voluptatem dolore! Voluptatum asperiores non nulla explicabo
 amet nobis laboriosam repudiandae cumque minus quaerat saepe veritatis iste ducimus, minima error quas?
  Architecto iusto sit debitis explicabo, vel incidunt ullam nisi. Neque beatae veniam amet velit! Voluptatibus,
   excepturi. Magnam, similique quos earum enim, neque accusamus corrupti, commodi nam veritatis sunt atque? Possimus,
    iure veritatis. Ipsam eos libero ut alias animi amet magni architecto voluptatibus in maiores iure, incidunt nulla
     perferendis saepe eum natus obcaecati illo eveniet? Et voluptatem recusandae delectus asperiores, in ipsam tempora 
     porro ex odit nisi iste, dolorem unde at aut rerum cum ad adipisci iusto veniam quisquam dolorum, id fuga quas 
     nostrum. Perferendis culpa enim necessitatibus soluta deserunt corporis sapiente quos similique maiores fuga 
     consectetur, repellendus aut, eos nisi, odit in doloribus veniam eum possimus animi dolore. Veritatis omnis 
     illum, blanditiis consequuntur animi atque cum dolorum saepe cumque doloremque hic sed sint! Nisi, distinctio 
     totam. Ipsum obcaecati fugit officiis in alias nemo qui, quaerat ipsam molestias, eligendi corrupti ducimus 
     veritatis dicta nam iusto debitis, mollitia impedit distinctio quisquam suscipit eius ut dolores possimus iste?
      Cum deserunt fuga perferendis modi fugit harum libero, architecto aspernatur veniam, nemo quae et excepturi,
       quas ab sint. Ex ipsa sint autem quod illo aut quisquam tenetur voluptatibus, minus at, aperiam amet iste 
       similique, error enim omnis quis distinctio temporibus saepe? Omnis incidunt exercitationem tempora corrupti 
       perferendis quisquam magnam quidem voluptatibus inventore delectus a quasi placeat facilis iure nisi veniam 
       officia mollitia, iste reiciendis doloribus voluptas aliquid at modi. Voluptatum ad ratione eos quidem 
       necessitatibus magni, ipsa odit, enim odio natus quod vel? Velit soluta hic temporibus, mollitia quam beatae 
       facere sequi numquam sapiente quia cupiditate maiores neque nihil, aspernatur vitae et sed assumenda odit sunt 
       eligendi id architecto iste? Odio corrupti autem quasi molestias, nesciunt error fugit perspiciatis tempore id, 
       sit tempora eos rerum magni officia ex quibusdam corporis? Aspernatur, consequuntur excepturi. 
       Tempora voluptate qui deserunt quo, at illum sit esse assumenda sint cumque maxime inventore vero, 
       saepe totam voluptates minima exercitationem provident nam veniam delectus expedita ea? Ipsa iste cupiditate 
       officia! Qui, quis facere illo quod laudantium impedit ipsum et aut eligendi, atque accusantium optio voluptate 
       expedita voluptates cumque! Sapiente quasi eum vero accusamus numquam corrupti repellat voluptatem laudantium 
       quam consectetur assumenda saepe ratione sit minus, modi sed sequi excepturi molestias eligendi tempora 
       blanditiis dolor? Excepturi deserunt commodi sit error perferendis nesciunt earum accusantium possimus 
       architecto necessitatibus ipsa esse, quas voluptates ratione numquam facilis odio! Iure, quos ut eius, qui, 
       deleniti necessitatibus doloremque sequi fuga amet reprehenderit sd porro velit voluptas tempora ducimus
        dolorem facere harum ratione numquam? Sequi ea ratione nemo neque asperiores quos culpa assumenda 
        voluptatum quo accusamus, quis iste earum eaque totam aliquam laudantium officiis ducimus ipsum magni 
        omnis rem itaque animi autem. Vel non in itaque sequi, laudantium recusandae culpa blanditiis nemo illo 
        laborum deleniti doloremque!"""

x = lorem.split()

e = input("Ingrese una letra para buscar palabras que empiezen con ella ")

count = 0
while count < len(x):
    if x[count].startswith(e):
        print(x[count])
    count += 1
